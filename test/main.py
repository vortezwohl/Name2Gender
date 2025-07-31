from name2gender import Name2Gender

if __name__ == '__main__':
    n2g = Name2Gender()
    names = ['吴子豪', '吴彦祖', '梅艳芳', '张曼玉',
             'Donald Trump', 'Ivanka Trump',
             'Justin Bieber', 'The Weeknd',
             'Luigi Nicholas Mangione',
             'Elizabeth II', 'Henry VIII']
    for name in names:
        _gender, _prob = n2g(name, return_probability=True)
        print(name, 'is', _gender, 'with a probability of', f'{_prob * 100:.2f}%')
