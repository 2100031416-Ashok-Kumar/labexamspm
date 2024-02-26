def main():
    ch = ['a', 'b', 'c']
    permute(ch, 0)

def permute(ch, fi):
    if fi == len(ch) - 1:
        print(''.join(ch))
        return
    for i in range(fi, len(ch)):
        ch[fi], ch[i] = ch[i], ch[fi]
        permute(ch, fi + 1)
        ch[fi], ch[i] = ch[i], ch[fi]

if __name__ == "__main__":
    main()
