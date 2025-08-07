from name2gender import Name2Gender, load_model

if __name__ == '__main__':
    n2g = Name2Gender(load_model('name2gender-small-en'))
    names = ['吴子豪', '吴彦祖', '梅艳芳', '张曼玉',
             'Donald Trump', 'Ivanka Trump',
             'Justin Bieber', 'The Weeknd',
             'Luigi Nicholas Mangione',
             'Elizabeth II', 'Henry VIII']
    for name in names:
        _gender, _prob = n2g(name, return_probability=True)
        print(name, 'is <', _gender, '> with a probability of', f'{_prob * 100:.2f}%')
