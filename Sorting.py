import random;

def generateFakeData(n):
    fakeData = list(range(n));
    random.shuffle(fakeData);
    return fakeData;

class BubbleSort:
    def BubbleSort(unsorted):
        for sortPath in range(len(unsorted) - 1):
            for index in range(len(unsorted) - 1):
                if unsorted[index] > unsorted[index + 1]:
                    temp = unsorted[index];
                    unsorted[index] = unsorted[index + 1];
                    unsorted[index + 1] = temp;
        return unsorted;

    def BubbleSortRecursive(unsorted, changed=False):
        for index in range(len(unsorted) - 1):
            if unsorted[index] > unsorted[index + 1]:
                temp = unsorted[index];
                unsorted[index] = unsorted[index + 1];
                unsorted[index + 1] = temp;
                changed = True;
        
        if changed == False:
            return unsorted;
        return BubbleSort.BubbleSortRecursive(unsorted, False);

class InsersionSort:
    def InsersionSort(unsorted):
        for index in range(len(unsorted) - 1):
            if unsorted[index] > unsorted[index + 1]:
                temp = unsorted[index];
                unsorted[index] = unsorted[index + 1];
                unsorted[index + 1] = temp;

                for index2 in range(index):
                    if unsorted[index2] > unsorted[index]:
                        temp = unsorted[index2];
                        unsorted[index2] = unsorted[index];
                        unsorted[index] = temp;
        return unsorted;

trial1 = generateFakeData(100);

print(trial1);
print(InsersionSort.InsersionSortRecursive(trial1))


