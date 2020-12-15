import unittest

from src.music_bracket import Song, MusicBracket, Bracket


class StandardItems:

    @staticmethod
    def standard_bracket():
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

        test_music_draft.create_bracket()

        for x in range(8):
            test_music_draft.vote(x, 3, 2)

        for x in range(4):
            test_music_draft.promote()

        for x in range(8, 12):
            test_music_draft.vote(x, 2, 3)

        for x in range(2):
            test_music_draft.promote()

        for x in range(12, 14):
            test_music_draft.vote(x, 2, 3)

        for x in range(1):
            test_music_draft.promote()

        test_music_draft.vote(14, 3, 3)


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("test_song_name", "test_artist_name")

    def test_create_song(self):
        self.assertEqual(str(self.song),
                         'test_song_name by test_artist_name',
                         "Song output for original input is incorrect")

    def test_create_set_song(self):
        self.song.set_name("test_alternate_song_name")
        self.assertEqual(str(self.song),
                         'test_alternate_song_name by test_artist_name',
                         "Song output for 1st alternate input is incorrect")

    def test_create_set_set_song(self):
        self.song.set_name("test_alternate_song_name")
        self.song.set_artist("test_alternate_artist_name")
        self.assertEqual(str(self.song),
                         'test_alternate_song_name by test_alternate_artist_name',
                         "Song output for 2nd alternate input is incorrect")

    def test_song_none(self):
        test = Song(None, None)
        self.assertEqual(str(test), 'None by None')

    def test_song_int_input(self):
        test = Song(5, 2)
        self.assertEqual(str(test), '5 by 2')

    def test_song_tuple_input(self):
        test = Song(("Song", "name"), ("Artist", "Name"))
        self.assertEqual(str(test), '(\'Song\', \'name\') by (\'Artist\', \'Name\')')


class TestBracket(unittest.TestCase):
    def setUp(self):
        self.song_name = "test_song_name"
        self.alternate_song_name = "test_alternate_song_name"
        self.artist_name = "test_artist_name"
        self.alternate_artist_name = "test_alternate_artist_name"
        self.bracket_number = 0

        self.first_song = Song(self.song_name, self.artist_name)
        self.second_song = Song(self.alternate_song_name, self.alternate_artist_name)

        self.bracket = Bracket(self.first_song, self.second_song, self.bracket_number)

    def test_create_bracket_blank(self):
        self.assertEqual(str(self.bracket), 'Bracket 0: ' + self.song_name + ' by '
                         + self.artist_name + ' vs ' + self.alternate_song_name + ' by '
                         + self.alternate_artist_name)

    def test_bracket_first_song_winner(self):
        self.bracket.vote(1, 3)
        self.assertEqual(str(self.bracket), 'Bracket 0: Winner ' + self.alternate_song_name
                         + ' by ' + self.alternate_artist_name + ' with 3 votes, Loser '
                         + self.song_name + ' by ' + self.artist_name + ' with 1 votes')

    def test_bracket_second_song_winner(self):
        self.bracket.vote(3, 1)
        self.assertEqual(str(self.bracket), 'Bracket 0: Winner ' + str(self.first_song)
                         + ' with 3 votes, Loser ' + str(self.second_song) + ' with 1 votes')

    def test_bracket_tie(self):
        test = Bracket(self.first_song, self.second_song, self.bracket_number)
        test.vote(3, 3)
        test_list = ['Bracket 0: Winner ' + str(self.first_song) + ' with 3 votes, Loser '
                     + str(self.second_song) + ' with 3 votes',
                     'Bracket 0: Winner ' + str(self.second_song) + ' with 3 votes, Loser '
                     + str(self.first_song) + ' with 3 votes']
        self.assertIn(str(test), test_list)


class TestMusicBracket(unittest.TestCase):
    def setUp(self):
        pass

    def test_music_bracket_creation(self):
        pass

    def test_music_bracket_creation_bad_bracket_size_minus_input(self):
        pass

    def test_music_bracket_creation_bad_bracket_size_invalid_input(self):
        pass

    def test_music_bracket_add_song(self):
        pass

    def test_music_bracket_add_wildcard(self):
        pass

    def test_music_bracket_pick_random_wildcard_song(self):
        pass

    def test_music_bracket_add_wildcard_to_songs(self):
        pass

    def test_music_bracket_pick_random_song(self):
        pass

    def test_music_bracket_dictionary_output(self):
        pass

    def test_music_bracket_get_bracket(self):
        pass

    def test_music_bracket_get_empty_bracket(self):
        pass

    def test_music_bracket_vote(self):
        pass

    def test_music_bracket_vote_none_bracket(self):
        pass

    def test_music_bracket_promote(self):
        pass

    def test_music_bracket_promote_none_bracket(self):
        pass

    def test_music_bracket_promote_none_winner(self):
        pass


if __name__ == '__main__':
    unittest.main()
