class InsersionSort:
    # These methods dont return a sorted array, they modify the array passed to it
    
    def InsersionSort(unsorted):
        steps = [];
        for index in range(len(unsorted) - 1):
            if unsorted[index] > unsorted[index + 1]:
                temp = unsorted[index];
                unsorted[index] = unsorted[index + 1];
                unsorted[index + 1] = temp;
                steps.append(f"Swapped {temp} and {unsorted[index]} around")

                for index2 in range(index):
                    if unsorted[index2] > unsorted[index]:
                        temp = unsorted[index2];
                        unsorted[index2] = unsorted[index];
                        unsorted[index] = temp;
                        steps.append(f"Swapped {temp} and {unsorted[index2]} around")
        return steps;
