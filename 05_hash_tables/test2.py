# -*- coding: utf-8 -*-
# 散列表用于防止重复

def check_voter(voted, name):
    if voted.get(name):
        print("Kick him/her out!")
    else:
        voted[name] = True
        print("Let him/her vote!")

def main():
    voted = {}
    check_voter(voted, "Tom")
    check_voter(voted, "Mike")
    check_voter(voted, "Mike")

if __name__ == "__main__":
    main()