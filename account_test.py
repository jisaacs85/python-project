import unittest
import account as AccountClass


class Test(unittest.TestCase):
    accInfo = AccountClass.Account()

    def test_check_password_length(self):
        print("Check possible passwords\n")
        password_list = ['abeautifilday', 'astrictboss', 'alovelyhouse']

        for passwd in password_list:
            print("Checking password " + passwd + "\n")
            pass_info = self.accInfo.check_password_length(passwd)
            self.assertTrue(pass_info)


if __name__ == '__main__':
    unittest.main()
