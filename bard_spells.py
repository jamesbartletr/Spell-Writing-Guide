from writer import load_attribute
import librosa


# Class for defining and using a musical scale
class scale():
    def __init__(self, steps, max_L, f0=440):
        """
        Initialize a musical scale.

        Args:
            steps (str): A string representing step intervals in semitones.
                         Example: "2212221" for a major scale.
            max_L (int): The maximum length for the scale.
            f0 (float): Base frequency (default is 440 Hz, which is standard A4).
        """
        n = [0]

        # Generate relative positions in the scale based on step intervals
        while len(n) < max_L:
            for s in list(steps):
                n.append(n[-1] + int(s))

        self.n = n  # List of relative note positions
        self.f0 = f0  # Base frequency

    def get_note(self, i):
        """
        Get the frequency of the i-th note in the scale.

        Args:
            i (int): Index of the note in the scale.

        Returns:
            float: Frequency of the note in Hz.
        """
        N = self.n[i]  # Get the relative position in the scale
        a = (2) ** (1 / 12)  # Equal temperament semitone ratio
        f = self.f0 * a ** N  # Calculate frequency
        return f


# Function to create a set of frequencies (chords) based on various Attributes
def chords_maker(rang, level, area, dtype, school, scale_steps="2212221", f0=440):
    """
    Generates musical chord frequencies based on given Attributes.

    Args:
        rang (str): Range attribute (e.g., 'point (150 feet)').
        level (str): Level attribute (e.g., '3').
        area (str): Area type attribute (e.g., 'sphere').
        dtype (str): Damage type attribute (e.g., 'fire').
        school (str): School attribute (e.g., 'evocation').
        scale_steps (str): Step intervals for the scale (default is major scale).
        f0 (float): Base frequency (default is 440 Hz).

    Returns:
        list: A list of frequencies (in Hz) representing the chord.
    """
    # Load attribute lists from external files
    ranges = load_attribute("Attributes/range.txt")
    levels = load_attribute("Attributes/levels.txt")
    area_types = load_attribute("Attributes/area_types.txt")
    dtypes = load_attribute("Attributes/damage_types.txt")
    schools = load_attribute("Attributes/school.txt")

    # Calculate the length of each attribute list
    lens = [len(ranges), len(levels), len(area_types), len(dtypes), len(schools)]

    # Reference scale for mapping attribute indices to frequencies
    reference_scale = scale(scale_steps, max_L=max(lens), f0=f0)

    # Find indices of the provided Attributes in their respective lists
    i_range = ranges.index(rang)
    i_levels = levels.index(level)
    i_area = area_types.index(area)
    i_dtype = dtypes.index(dtype)
    i_school = schools.index(school)

    attr = [i_range, i_levels, i_area, i_dtype, i_school]

    # Ensure all indices are unique by resolving duplicates
    while len(set(attr)) != len(attr):
        seen = []
        for i, a in enumerate(attr):
            if a in seen:
                attr[i] += lens[i]  # Adjust duplicate indices
            else:
                seen.append(a)

    # Generate frequencies for the Attributes
    f = []
    for i in attr:
        f.append(reference_scale.get_note(i))

    return f


if __name__ == "__main__":
    # Example scales
    major = "2212221"  # Major scale intervals
    minor = "2122122"  # Minor scale intervals
    blues = "321132"  # Blues scale intervals

    # Example base frequencies
    A4 = 440  # Standard A4 frequency
    Middle_C = 264  # Frequency of middle C

    # Generate chords based on the given Attributes
    f = chords_maker(
        'point (150 feet)', '3', "sphere", "fire", "evocation",
        scale_steps=blues, f0=Middle_C
    )

    # Convert and print the frequencies as note names
    for f_ in f:
        print(librosa.hz_to_note(f_))
