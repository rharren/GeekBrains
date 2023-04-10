/*Задача:
Написать программу, которая из имеющегося массива строк формирует новый массив из строк,
длина которых меньше, либо равна 3 символам. Первоначальный массив можно ввести с клавиатуры,
либо задать на старте выполнения алгоритма. При решении не рекомендуется пользоваться коллекциями,
лучше обойтись исключительно массивами.

Примеры:

[“Hello”, “2”, “world”, “:-)”] → [“2”, “:-)”]
[“1234”, “1567”, “-2”, “computer science”] → [“-2”]
[“Russia”, “Denmark”, “Kazan”] → []
*/

string[] test1 = {"hello","2","world", ":-)"};
string[] test2 = {"1234","1567","-2","computer science"}; 
string[] test3 = {"Russia","Denmark","Kazan"};
PrintArray(test1);
PrintArray(test2);
PrintArray(test3);


//  Функция вывода массива в терминал
void PrintArray(string[] array)
{
    Console.WriteLine();
    Console.Write("Массив: [");
    string[] NewArray = new string[] {};
    // доп функция для распечатки элементов массивов
    void ArrConsolPrint  (string element, int i, int ArrLen)
        {
            if (i == ArrLen)
            {
                Console.Write("“{0}“", element);
            }
            else
            { 
                Console.Write("“{0}“, ", element);
            }
        }
    // Работа с массивом который дали на проверку
    for (int i=0; i <= array.Length-1; i++)
    {   
        if (array[i].Length <=3)
        {
            NewArray = NewArray.Append(array[i]).ToArray();
        }
        
        ArrConsolPrint(array[i], i, array.Length-1);
    }
    Console.Write("] → [");
    // Работа с массивом который хотим получить
    for (int j=0; j <= NewArray.Length-1; j++)
    {   
        ArrConsolPrint(NewArray[j], j, NewArray.Length-1);
    }
    Console.Write(']');
}