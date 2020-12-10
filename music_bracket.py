import random

"""
This Class holds all the songs, wildcard songs and brackets in lists.
After construction you can input the songs and randomly generate a bracket. This may include selecting wildcard songs.
You may then input the votes and promote the brackets.
New brackets will be places at the end of the list.
"""


class MusicBracket:
    def __init__(self, bracket_size):
        check = bracket_size
        while check > 0:
            if check % 2 > 0:
                try:
                    raise ValueError('Bracket size not divisible by 2')
                except ValueError:
                    print(check)
                    raise
            check = check / 2
            if check == 1:
                break

        self.songs = []
        self.wildcard_songs = []
        self.bracket_size = bracket_size
        self.bracket = []

    def add_song(self, song):
        self.songs.append(song)

    def add_wildcard(self, song):
        self.wildcard_songs.append(song)

    def pick_random_wildcard(self):
        return self.wildcard_songs[random.randint(0, len(self.wildcard_songs) - 1)]

    def add_wildcard_to_songs(self):
        selected_song = self.pick_random_wildcard()
        self.songs.append(selected_song)
        self.wildcard_songs.remove(selected_song)
        return selected_song

    def output(self):
        return dict(Songs=self.songs,
                    Wildcard_Songs=self.wildcard_songs,
                    Bracket_Size=self.bracket_size)

    def pick_random_song(self):
        return self.songs[random.randint(0, len(self.songs) - 1)]

    def create_bracket(self):
        for i in range(int(self.bracket_size / 2)):
            song_a = self.pick_random_song()
            self.songs.remove(song_a)

            song_b = self.pick_random_song()
            self.songs.remove(song_b)

            self.bracket.append(Bracket(song_a, song_b, i + 1))

    def get_bracket(self):
        output = ""
        for i in range(len(self.bracket)):
            output += str(self.bracket[x]) + '\n'
        return output

    def vote(self, bracket_num, song_a_votes, song_b_votes):
        self.bracket[bracket_num].vote(song_a_votes, song_b_votes)
        return self.bracket[bracket_num]

    def promote(self):
        self.bracket.append(Bracket(self.bracket[
                                        len(self.bracket) - (self.bracket_size - len(self.bracket))].winner,
                                    self.bracket[
                                        len(self.bracket) - (self.bracket_size - len(self.bracket)) + 1].winner,
                                    len(self.bracket) + 1))


"""
These are the brackets used in the MusicBracket class.
They will contain 2 songs and the votes for each song.
After voting happens a winner will be declared in the bracket.
In the event of a tie, a winner will be declared randomly.
"""


class Bracket:
    def __init__(self, song_a, song_b, bracket_number):
        self.song_a = song_a
        self.song_b = song_b
        self.a_votes = 0
        self.b_votes = 0
        self.bracket_number = bracket_number
        self.winner = None

    def __repr__(self):
        if self.winner is None:
            return "Bracket %s: %s vs %s" % (self.bracket_number,
                                             self.song_a, self.song_b)

        if self.winner == self.song_a:
            return "Bracket %s: Winner %s with %s votes, Loser %s with %s votes" % (self.bracket_number,
                                                                                    self.song_a, self.a_votes,
                                                                                    self.song_b, self.b_votes)

        else:
            return "Bracket %s: Winner %s with %s votes, Loser %s with %s votes" % (self.bracket_number,
                                                                                    self.song_b, self.b_votes,
                                                                                    self.song_a, self.a_votes)

    def vote(self, song_a_votes, song_b_votes):
        self.a_votes = song_a_votes
        self.b_votes = song_b_votes

        if self.a_votes > self.b_votes:
            self.winner = self.song_a
        elif self.a_votes < self.b_votes:
            self.winner = self.song_b
        else:
            if random.randint(0, 1) == 0:
                self.winner = self.song_a
            else:
                self.winner = self.song_b

        return self.winner


"""
This class will contain the artist and the song name.
"""


class Song:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist

    def __repr__(self):
        return "%s by %s" % (self.name, self.artist)

    def set_name(self, name):
        self.name = name

    def set_artist(self, name):
        self.artist = name


class Interface:
    def __init__(self):
        self.bracket = MusicBracket(input("Bracket size (Must be a power of 2): "))

    def input_song(self):
        self.bracket.add_song(Song(input("Song name: "), input("Artist name: ")))

    def input_wildcard_song(self):
        self.bracket.add_wildcard(Song(input("Song name: "), input("Artist name: ")))


song1 = Song("Dragonball Durag", "Thundercat")
song2 = Song("In Too Deep", "Eminem")
song3 = Song("I Won't Be Home for Christmas", "Poppy")
song4 = Song("Heat Waves", "Glass Animals")
song5 = Song("All I Need", "Jacob Collier")
song6 = Song("Better - Radio Edit", "Jack Garratt")
song7 = Song("Draw the Line", "David Larbi")
song8 = Song("Revenge", "Joyner Lucas")
song9 = Song("Break My Heart Again", "Finneas")
song10 = Song("My Agenda", "Dorian Electra")
song11 = Song("Let's Fall in Love for the Night", "Finneas")
song12 = Song("The Lighthouse Keeper", "Sam Smith")
song13 = Song("Run", "Joji")
song14 = Song("Leave Me Alone", "I DON'T KNOW HOW BUT THEY FOUND ME")
song15 = Song("Bad Friend", "Rina Sawayama")

wildcard1 = Song("Mr Experience", "Donny Benet")
wildcard2 = Song("The Hungry Wolf of Fate", "King Gizzard & The Lizzard Wizard")
wildcard3 = Song("Without Me", "Halsey")
wildcard4 = Song("You Should Be Sad", "Halsey")
wildcard5 = Song("That Won't Save Us", "Against The Current")

test_music_draft = MusicBracket(16)
test_music_draft.add_song(song1)
test_music_draft.add_song(song2)
test_music_draft.add_song(song3)
test_music_draft.add_song(song4)
test_music_draft.add_song(song5)
test_music_draft.add_song(song6)
test_music_draft.add_song(song7)
test_music_draft.add_song(song8)
test_music_draft.add_song(song9)
test_music_draft.add_song(song10)
test_music_draft.add_song(song11)
test_music_draft.add_song(song12)
test_music_draft.add_song(song13)
test_music_draft.add_song(song14)
test_music_draft.add_song(song15)

test_music_draft.add_wildcard(wildcard1)
test_music_draft.add_wildcard(wildcard2)
test_music_draft.add_wildcard(wildcard3)
test_music_draft.add_wildcard(wildcard4)
test_music_draft.add_wildcard(wildcard5)

print("Wildcard song is: " + str(test_music_draft.add_wildcard_to_songs()) + "\n")
test_music_draft.create_bracket()
print(test_music_draft.get_bracket())

for x in range(8):
    test_music_draft.vote(x, 3, 2)

print(test_music_draft.get_bracket())

for x in range(4):
    test_music_draft.promote()

print(test_music_draft.get_bracket())

for x in range(8, 12):
    test_music_draft.vote(x, 2, 3)

print(test_music_draft.get_bracket())

for x in range(2):
    test_music_draft.promote()

print(test_music_draft.get_bracket())

for x in range(12, 14):
    test_music_draft.vote(x, 2, 3)

print(test_music_draft.get_bracket())

for x in range(1):
    test_music_draft.promote()

print(test_music_draft.get_bracket())

test_music_draft.vote(14, 3, 3)
print(test_music_draft.get_bracket())
