# https://leetcode.com/problems/simplify-path/

# the key is to get rid of the "//" and only analyze the "real" componnents
# if ".", continue to the next element
# if "..", if there are existing subdirectory, then pop it off
# else if already in root directory, continue to the next element
# append other subdir elements to the list normally
# finally join the valid subdirectories by "/" and put another "/" in front.

def simplifyPath(self, path: str) -> str:
        path2 = [i for i in path.split("/") if i != ""]
        subdir = []
        for ele in path2:
            if ele == ".":
                continue
            elif ele =="..":
                if not subdir:
                    continue
                else:
                    subdir.pop()
            else:
                subdir.append(ele)
        return "/" + "/".join(subdir) 