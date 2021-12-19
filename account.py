class Account:
    @staticmethod
    def check_password_length(password):
        if len(password) > 8:
            return True
        else:
            return False


if __name__ == '__main__':
    accVerify = Account()
    print('The password length is ' + str(accVerify.check_password_length('offtoschool')))
