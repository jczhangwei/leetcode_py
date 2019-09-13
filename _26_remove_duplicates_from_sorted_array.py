
class Sollution:
    def removeDuplicates(self, nums):
        i = 0
        temp = None
        while i < len(nums):
            if temp == nums[i]:
                nums.pop(i)
            else:
                temp = nums[i]
                i = i + 1

        return len(nums)

    def doTest(self):
        case = [1, 1, 2, 2, 2, 3, 4, 5, 5]
        nums = list(case)
        self.removeDuplicates(nums)
        print("removeDuplicates: ", nums)
