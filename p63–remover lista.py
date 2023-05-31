# Remover elementos de la lista 
import os; os.system('cls')

nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100] 
print(f'Todos los números : {nums} - {len(nums)} \n')
nums.remove(99)
print(f'Remover primera ocurrencia : {nums} - {len(nums)} \n') 
num=nums.pop(8)
print(f'Remover elemento en una posicion y ponerlo en otra variable: {nums} - {num} - {len(nums)}\n') 
num=nums.pop()
print(f'Remover el ultimo elemento: : {nums} - {num} - {len(nums)}\n') 
nums.clear()
print(f'Remover todos : {nums} - {len(nums)}\n')