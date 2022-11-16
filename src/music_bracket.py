import random

"""
This Class holds all the songs, wildcard songs and brackets in lists.
After construction you can input the songs and randomly generate a bracket. This may include selecting wildcard songs.
You may then input the votes and promote the brackets.
New brackets will be places at the end of the list.
"""


class MusicBracket:
    def __init__(self, bracket_size):
        if bracket_size <= 0:
            raise ValueError('Bracket is not a positive integer')
        check = bracket_size
        while check > 0:
            if check % 2 > 0:
                raise ValueError('Bracket size not divisible by 2')
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

    def move_wildcard_to_songs(self):
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
        if len(self.bracket) > 0:
            raise Exception("Bracket has already been generated!")

        for i in range(int(self.bracket_size / 2)):
            song_a = self.pick_random_song()
            self.songs.remove(song_a)

            song_b = self.pick_random_song()
            self.songs.remove(song_b)

            self.bracket.append(Bracket(song_a, song_b, i + 1))

    def get_bracket(self):
        output = ""
        for i in range(len(self.bracket)):
            output += str(self.bracket[i]) + '\n'
        return output

    def vote(self, bracket_num, song_a_votes, song_b_votes):
        self.bracket[bracket_num].vote(song_a_votes, song_b_votes)
        return self.bracket[bracket_num]

    def promote(self):
        bracket_a = self.bracket[len(self.bracket) - (self.bracket_size - len(self.bracket))]
        bracket_b = self.bracket[len(self.bracket) - (self.bracket_size - len(self.bracket)) + 1]

        if bracket_a.winner is None:
            raise ValueError("Bracket " + str(bracket_a.bracket_number) + " is None!")

        if bracket_b.winner is None:
            raise ValueError("Bracket" + str(bracket_b.bracket_number) + " is None!")

        self.bracket.append(Bracket(bracket_a.winner, bracket_b.winner, len(self.bracket) + 1))


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
    def __init__(self, name, artist, picker=0):
        self.name = name
        self.artist = artist
        self.picker = picker

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


# music_bracket = MusicBracket(8)
#
# music_bracket.add_song(Song("1", "_"))
# music_bracket.add_song(Song("2", "_"))
# music_bracket.add_song(Song("3", "_"))
# music_bracket.add_song(Song("4", "_"))
# music_bracket.add_song(Song("5", "_"))
# music_bracket.add_song(Song("6", "_"))
# music_bracket.add_song(Song("7", "_"))
# music_bracket.add_song(Song("8", "_"))
#
# music_bracket.create_bracket()
#
# print(music_bracket.get_bracket())
