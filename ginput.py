def get_input(data, text):
    cnt = 0
    while True:
        try:
            return data(input(f'{text}'))
        except ValueError:
            print('\nThe number you inserted is not on the correct format, try again\n')
            cnt += 1
        if cnt > 2:
            print(f'The data type you should provide is of {data} type, try again\n')



def main():
    x = get_input(int, 'Insert an int: ')
    print(x)


if __name__ == '__main__':
    main()
