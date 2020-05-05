print('以下の数字で座標を指定してください')
text = """
1|2|3
-----
4|5|6
-----
7|8|9
"""
#文字列として複数行を入力する場合、3つつけて囲む。
print(text)

numbers = [1,2,3,4,5,6,7,8,9]
maru = []# maru = []　に仮に2,3,6がinputされたと仮定しmaru = [2,3,6]とする
batsu = []
n = 0

def number(lis):#def number(lis):のlisに [2,3,6]が渡される
    if [1, 2, 3] == list(set([1, 2, 3]) & set(lis)):#1，2，3というリストと入力によって作ったリスト、このそれぞれがset型になったもの
        return True
    if [4, 5, 6] == list(set([4, 5, 6]) & set(lis)):
        return True
    if [7, 8, 9] == list(set([7, 8, 9]) & set(lis)):
        return True
    if [1, 4, 7] == list(set([1, 4, 7]) & set(lis)):
        return True
    if [2, 5, 8] == list(set([2, 5, 8]) & set(lis)):
        return True
    if [3, 6, 9] == list(set([3, 6, 9]) & set(lis)):
        return True
    if [1, 5, 9] == list(set([1, 5, 9]) & set(lis)):
        return True
    if [3, 5, 7] == list(set([3, 5, 7]) & set(lis)):
        return True
    return False

while True:
    if n % 2 == 0:
        senkou = input("先攻の座標は？")#inputした値は変数senkouに代入される
        try:
            senkou = int(senkou)
        except:
            print("正しい座標を入力してください")
            continue
        if senkou in numbers:
            text = text.replace(str(senkou), "o")
            numbers.remove(senkou)
            maru.append(senkou)#maru.append(senkou)でsenkouの内容は maru = []の末尾に追加されていく
            print(text)
            if number(maru):
                print("先攻の勝ち")
                break
        else:
            print("正しい座標を入力してください")
            continue
        n += 1
        print(n)
    else:
        koukou =input("後攻の座標は？")
        try:
            koukou = int(koukou)
        except:
            print("正しい座標を入力してください")
        if koukou in numbers:
            text = text.replace(str(koukou), "x")
            numbers.remove(koukou)
            batsu.append(koukou)
            print(text)
            if number(batsu):
                print("後攻の勝ち")
                break
        else:
            print("正しい座標を入力してください")
            continue

        n += 1
        print(n)
        
    if n == 9:
        print("決着つきません")            
        break        