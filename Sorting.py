import random;
import copy;

from BubbleSort import BubbleSort
from InsersionSort import InsersionSort

def generateFakeData(n):
    fakeData = list(range(n));
    random.shuffle(fakeData);
    return fakeData;

def RunAndLogBubbleSort():
    trial = generateFakeData(100);
    trialCopy = copy.copy(trial);
    steps = BubbleSort.BubbleSort(trialCopy);

    with open("./BubbleSortSteps.txt", "w+") as fileWriter:
        fileWriter.write("\n".join([f"Starting Data:\n{str(trial)}\n", "Steps:"] + steps + [f"\nResulting Data:\n{str(trialCopy)}"]));

def RunAndLogBubbleSortRecursive():
    trial = generateFakeData(100);
    trialCopy = copy.copy(trial);
    steps = BubbleSort.BubbleSortRecursive(trialCopy);

    with open("./BubbleSortRecursiveSteps.txt", "w+") as fileWriter:
        fileWriter.write("\n".join([f"Starting Data:\n{str(trial)}\n", "Steps:"] + steps + [f"\nResulting Data:\n{str(trialCopy)}"]));

def RunAndLogInsersionSort():
    trial = generateFakeData(100);
    trialCopy = copy.copy(trial);
    steps = InsersionSort.InsersionSort(trialCopy);

    with open("./InsersionSortSteps.txt", "w+") as fileWriter:
        fileWriter.write("\n".join([f"Starting Data:\n{str(trial)}\n", "Steps:"] + steps + [f"\nResulting Data:\n{str(trialCopy)}"]));

RunAndLogBubbleSort()
RunAndLogBubbleSortRecursive()
RunAndLogInsersionSort()
