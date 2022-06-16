class BubbleSort:
    # These methods dont return a sorted array, they modify the array passed to it

    def BubbleSort(unsorted):
        steps = [];
        for sortPath in range(len(unsorted) - 1):
            for index in range(len(unsorted) - 1):
                if unsorted[index] > unsorted[index + 1]:
                    temp = unsorted[index];
                    unsorted[index] = unsorted[index + 1];
                    unsorted[index + 1] = temp;
                    steps.append(f"Swapped {temp} and {unsorted[index]} around");
                    
        steps.append("Successfully Sorted");
        return steps;

    def BubbleSortRecursive(unsorted, changed=False, steps=[]):
        for index in range(len(unsorted) - 1):
            if unsorted[index] > unsorted[index + 1]:
                temp = unsorted[index];
                unsorted[index] = unsorted[index + 1];
                unsorted[index + 1] = temp;
                steps.append(f"Swapped {temp} and {unsorted[index]} around");
                changed = True;
        
        if changed == False:
            return steps;
        return BubbleSort.BubbleSortRecursive(unsorted, False, steps);
