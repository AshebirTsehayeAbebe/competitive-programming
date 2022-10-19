"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(id)
        # dic = {}
        # sub = {}
        # for employee in employees:
        #     dic[employee.id] = employee.importance
        #     sub[employee.id] = employee.subordinates
        # def helper(id):
        #     res = dic[id]
        #     for sub_id in sub[id]:
        #         res += helper(sub_id)
        #     return res
        # return helper(id)
