#coding:utf-8
import itchat
import re


def qun_op_msg(msg):
    if msg["FromUserName"] == "@@f6c47f4349ae56e8abe9fe03ad0f195ab7ada89915a6279084f698d2612aa36a" and msg["IsAt"] == True:
        content = msg["Text"]
        if "的电话" in content:
            name = content.split("myname")[-1].split("的")[0].lstrip() #myname is Nickname
            with open("diag",'r') as f:
                md = [i.strip() for i in f.readlines()]
                for i in md:
                    if name in i:
                        return i
            return "未检索到" + name + "的电话"
        return 0



@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def show_content(msg):
    """
    with open("jilu.txt",'a+') as f:
        f.write('='*10 + '\n')
        for i in msg:
            if i == 'User':
                continue
            f.write(str(i) + ' : ' + str(msg[i]) + '\n')
            f.write('-'*10 + '\n')
    """
    print(msg["ActualNickName"] + ":" + msg["Text"])
    chuli = qun_op_msg(msg)
    if chuli != "0" and type(chuli) is str:
        itchat.send_msg(msg=chuli, toUserName="@@f6c47f4349ae56e8abe9fe03ad0f195ab7ada89915a6279084f698d2612aa36a")
        print("reply " + "@@f6c47f4349ae56e8abe9fe03ad0f195ab7ada89915a6279084f698d2612aa36a: " + chuli)
    
    # print('ok')

@itchat.msg_register(itchat.content.TEXT, isGroupChat=False)
def show_content(msg):
    with open("jilu.txt",'a+') as f:
        f.write('='*10 + '\n')
        for i in msg:
            if i == 'User':
                continue
            f.write(str(i) + ' : ' + str(msg[i]) + '\n')
            f.write('-'*10 + '\n')
    print(msg["Alias"] + ":" + msg["Text"])
    # print('ok')


def main():
    itchat.auto_login(True,enableCmdQR=2)
    my_user_name = itchat.get_friends(update=True)[0]["UserName"]
    print(my_user_name)
    itchat.run()

if __name__ == "__main__":
    main()
