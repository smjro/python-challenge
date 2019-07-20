# -*- coding: utf-8 -*-


def _caesar(c, num):
    """指定数文文字をシフト
    
    パラメータ
    ------------------
    c   : str
        文字
    num : int
        シフトする数
    
    """
    if 'A' <= c and c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + num) % 26 + ord('A'))

    if 'a' <= c and c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + num) % 26 + ord('a'))

    # その他の文字は対象外
    return c


def rot13(s, num=13):
    # ジェネレータ内包表記で文字列に ROT13 を適用する
    g = (_caesar(c, num) for c in s)
    # 文字列に直す
    return ''.join(g)


def main():
    s = "Uryyb, Jbeyq!"
    print(rot13(s))


if __name__ == '__main__':
    main()
