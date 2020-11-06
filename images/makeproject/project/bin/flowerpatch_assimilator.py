from assimilator import *
from Boinc import boinc_project_path
import re, os


re_result = re.compile(r"(?<=S: )\d{21}")
re_pattern_number = re.compile(r"(?<=Pattern: )\d+")
re_center_number = re.compile(r"(?<=Center: )\d+")

class FlowerPatchAssimilator(Assimilator):
    def __init__(self):
        Assimilator.__init__(self)

    def assimilate_handler(self, wu, results, canonical_result):
        if canonical_result == None:
            return
        
        path = boinc_project_path.project_path("flowerpatch_results")
        input_path = self.get_file_path(canonical_result)

        with open(input_path) as input_file:
            input_str = input_file.read()

        try:
            os.makedirs(path)
        except OSError:
             pass
        
        pattern_number = re_pattern_number.search(canonical_result).grpup(0)
        center_number = re_center_number.search(canonical_result).group(0)
        
        out_file =  "task_{}_{}.txt".format(str(pattern_number), str(center_number))
        with open(os.path.join(path, out_file), "a") as f:
		    for match in re_result.finditer(input_str):
                f.write(match.group(0))

if __name__ == "__main__":
    asm = FlowerPatchAssimilator()
    asm.run()