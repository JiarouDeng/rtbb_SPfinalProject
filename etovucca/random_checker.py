import hashlib, string, random


if __name__ == "__main__":
    str_const = "Matthew"
    random.seed(len(str_const))
    letters = string.ascii_letters + string.digits
    ounce = "".join(random.choice(letters) for _ in range(50))
    result_str = ounce + str_const + "2"
    hash_pswd = hashlib.md5(result_str.encode()).hexdigest()
    print(hash_pswd)
