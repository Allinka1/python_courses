# 3.Написать функцию перевода размеров женского белья из международного во все остальные. 
# Внтри функции нужно просто обращаться к правильно составленному словарю.


sizes_of_lingerie = {
                     'XXS': 'RU: 42, DE: 36, US: 8, FR: 38, GB: 24',
                     'XS': 'RU: 44, DE: 38, US: 10, FR: 40, GB: 26',
                     'S': 'RU: 46, DE: 40, US: 12, FR: 42, GB: 28',
                     'M': 'RU: 48, DE: 42, US: 14, FR: 44, GB: 30',
                     'L': 'RU: 50, DE: 44, US: 16, FR: 46, GB: 32',
                     'XL': 'RU: 52, DE: 46, US: 18, FR: 48, GB: 34',
                     'XXL': 'RU: 54, DE: 48, US: 20, FR: 50, GB: 36',
                     'XXXL': 'RU: 56, DE: 50, US: 22, FR: 52, GB: 38'
                     }


def sizes(d, size):
	size = size.upper()
	for k, v in sizes_of_lingerie.items():
		if k == size:
			return v


for_sizes = input('Please enter international size: ')
print(sizes(sizes_of_lingerie, for_sizes))