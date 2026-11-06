from streams import factorial_stream, take, drop, sliding_window
from itertools import islice

def main():
    print("Лабораторна робота 5 (Варіант 11: Послідовність факторіалів)")
    
    stream = factorial_stream()
    first_10 = take(10, stream)
    print(f"Перші 10 факторіалів (0! - 9!): {first_10}")
    
    stream2 = factorial_stream()
    next_5 = take(5, drop(5, stream2))
    print(f"Факторіали з 5! по 9! (drop 5, take 5): {next_5}")
    
    stream3 = factorial_stream()
    windows = list(islice(sliding_window(stream3, 3), 5))
    print(f"Перші 5 ковзних вікон (k=3) для факторіалів:")
    for w in windows:
        print(f"  {w}")

if __name__ == "__main__":
    main()
