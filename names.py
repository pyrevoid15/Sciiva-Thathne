import random

namepaks = [1, 2, 3]

name_roots = []

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'a', 'e', 'i', 'o', 'u', 'e']
consonants = ['b', 'c', 'd', 'f', 'g', 'j', 'k', 'm', 'n', 'p', 'q',
              's', 't', 'v', 'x', 'z', 'b', 'c', 'd','f', 'g',  'j',
              'k', 'm', 'n', 'p', 'q', 's', 't', 'v']
dipthongs = ['ch', 'zh', 'sh', 'th']
fluids = ['w', 'r', 'y', 'h', 'l']

suff_list = ['sk', 'fil', 'lai', 'pol', 'soto', 'liych', 'gi', 'masa', 'nar', 'mino', 'su', 'tag', 'sono', 'flu', 'no',
             'lo', 'da', 'ved', 'sha', 'zuma', 'lini', 'yari', 'za', 'de', 'szin', 'ne', 'enor', 'ka', 'us', 'a', 'bon',
             'sil', 'il', 'sin', 'le', 'nir', 'ira', 'ma', 'mei', 's', 'ing', 'eva']

def name_gen(order):
    list = []
    for _ in range(0, order):
        protoname = ''
        word_struct = ''
        for _ in range(0, random.randint(1, 4)):
            syllable = ''
            syll_struct = ''
            syll_len = random.randint(1, 4)
            for a in range(0, syll_len):
                if a == 0:
                    letter_type = random.choice(['v', 'c', 'd', 'f'])
                elif a < syll_len:
                    letter_type = random.choice(['v', 'c', 'f'])
                    if letter_type != 'v' and letter_type == syll_struct[a - 1]:
                        while letter_type == syll_struct[a - 1]:
                            letter_type = random.choice(['v', 'c', 'f'])
                else:
                    letter_type = random.choice(['v', 'c', 'f'])

                if letter_type == 'v':
                    letter = random.choice(vowels)
                elif letter_type == 'c':
                    letter = random.choice(consonants)
                elif letter_type == 'd':
                    letter = random.choice(dipthongs)
                elif letter_type == 'f':
                    letter = random.choice(fluids)
                else:
                    letter = 'o'

                if a > 1 and random.randint(0, 12) == 1:
                    break

                syll_struct += letter_type
                syllable += str(letter)

            protoname += syllable
            word_struct += syll_struct
        protoname += random.choice(suff_list)
        list.append(protoname.capitalize())
    return list


name_list = ['iyuozluw', 'ew', 'ug', 'nudithm', 'reguue', 'wrshaai', 'shhuthpal', 'yachne', 'iel', 'zhyera', 'ykece',
             'dej', 'shelt', 'girpiaex', 'hlayi', 'icea', 'thor', 'nyeafser' 'hkuyn', 'brshuiwa', 'chyiy', 'wath',
             'oocikee', 'shrsha', 'slthoy', 'cawy', 'wishbym', 'ylowoskr', 'vya', 'ha', 'chwldia', 'crio', 'ysrwkyzik',
             'holinrx', 'kef', 'zhoy', 'zhrsa', 'hvraia', 'lithwsiqua', 'la', 'hoaecth', 'rojurv' 'awsio', 'lor', 'yil',
             'eneaio', 'afzhvrn', 'dwu', 'kiek', 'tyelbyrn', 'gwey', 'mele', 'shuje', 'iwer', 'fauhe', 'uzoth', 'faf',
             'zhemrch','ilpo', 'nwash', 'yhlkeytth', 'kyj', 'esciiva', 'u', 'zhapre', 'peawa', 'mo', 'thahe', 'zhzirn',
             'yyel', 'yici', 'wui', 'zhgu', 'iya', 'flar', 'rbokei', 'zrurfacna', 'efuge', 'thulg', 'alikrch', 'yo',
             'isya', 'byo', 'd', 'fariu', 'raloo', 'eahzum', 'fyla', 'tyma', 'hjoi', 'el', 'dath', 'xasrmch', 'gnar',
             'reu', 'thnlexa', 'chema', 'zyim', 'etyo', 'ather', 'nymis', 'i', 'thath', 'sgau', 'ya', 'mish', 'penor',
             'e', 'zhnes', 'thilivl', 'pachx', 'efre', 'eryh', 'rre', 'oyyo', 'llj', 'egi', 'pyhu', 'zhbou', 'yezy',
             'zhogru', 'rtzhmi', 'shyth', 'zheu', 'hali', 'axluu', 'tyx', 'zheu', 'alich', 'xri', 'thar', 'pek',
             'chumeo', 'mona', 'shweca', 'byedo', 'do', 'chut', 'narli', 'yzh', 'jrov', 'cash', 'thiodch', 'xai',
             'arqwa', 'shyr', 'ev', 'tikhe', 'nych', 'biho', 'enye', 'wil', 'hod', 'uth', 'ychla', 'yb', 'om', 'rit',
             'cx', 'puyo', 'chcum', 'vald', 'juch', 'ar', 'agizhea', 'ho', 'ute', 'uboli', 'lepyn', 'nyj', 'shik', 'ugo'
             'he', 'biar', 'nlewi', 'chay', 'isho', 'deo', 'dia', 'theri', 'ye', 'theye', 'atiya', 'cheth', 'kocho', 'y'
             'n', 'dush', 'ulcr', 'mou', 'yach', 'zhre', 'cao', 'ornyo', 'huwi', 'wimo', 'gwe', 'weo', 'vech', 's',
             'aiho', 'goz', 'tlga', 'humwu', 'pyo', 'uirei', 'itis', 'yaqa', 'awdior', 'galol', 'ti', 'yeg', 'shwoomel',
             'thew', 'waya', 'lee', 'erla', 'duse', 'voz', 'pelo', 'cren', 'waan', 'cri', 'ky', 'orpi', 'oli', 'cren',
             'zhae', 'cla', 'ahoo', 'ihleli', 'syla', 'uani', 'lit', 'byili', 'cren', 'cren', 'wiwa', 'verta', 'sciiva',
             'chung', 'lin', 'tere', 'glae', 'ahiha', 'flo', 'lae', 'ada', 'eve', 'aki', 'shro', 'mahi', 'fro', 'beko',
             'sou', 'min', 'yao', 'poy', 'ma', 'lla', 'mei', 'one', 'oni', 'codo', 'uchu', 'hio', 'chrez', 'ste', 'ble',
             'dio', 'kare', 'cara', 'gy', 'guo', 'ileo', 'idi', 'pepe', 'althe', 'lcai', 'tesh', 'si', 'thano', 'eva']


def name_dump(order):
    names = ''
    for _ in range(0, order):
        names += "{} {}\n".format((random.choice(name_list) + random.choice([random.choice(suff_list), '', '', '', '', '', '', '', '', ''])).capitalize(), (random.choice(name_list) + random.choice(suff_list)).capitalize())
    return names

if __name__ == '__main__':
    print(name_gen(10))
    print(name_dump(50))

