# -*- coding: utf-8 -*-
# �t��k���R����
# �Ǹ�: 11020107 / 11020137 / 11020140
# �m�W: Ĭ�B�� / ������ / ���f��
# ����j�ǹq����T�Ǥh�Z

if __name__ == '__main__':
    answers = [__import__('11020107_1'), __import__('11020107_2'), __import__('11020107_3'), __import__('11020107_4'), __import__('11020107_5')]
    while True:
        try:
            command = int(input('Input command(0 for quit, 1~5 for questions 1~5): '))
            if command == 0:
                break
            elif 1 <= command and command <= 5:
                answers[command-1].main()
            else:
                print('Invalid command, try again.')
        except Exception as e:
            print('Invalid command or illegal input, try again.')