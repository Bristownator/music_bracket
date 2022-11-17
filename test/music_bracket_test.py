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
        self.assertEqual(self.song.picker, 0)

    def test_create_set_song(self):
        self.song.set_name("test_alternate_song_name")
        self.assertEqual(str(self.song),
                         'test_alternate_song_name by test_artist_name',
                         "Song output for 1st alternate input is incorrect")
        self.assertEqual(self.song.picker, 0)

    def test_create_set_set_song(self):
        self.song.set_name("test_alternate_song_name")
        self.song.set_artist("test_alternate_artist_name")
        self.assertEqual(str(self.song),
                         'test_alternate_song_name by test_alternate_artist_name',
                         "Song output for 2nd alternate input is incorrect")
        self.assertEqual(self.song.picker, 0)

    def test_song_none(self):
        test = Song(None, None, None)
        self.assertEqual(str(test), 'None by None')
        self.assertEqual(test.picker, None)

    def test_song_int_input(self):
        test = Song(5, 2)
        self.assertEqual(str(test), '5 by 2')

    def test_song_tuple_input(self):
        test = Song(("Song", "name"), ("Artist", "Name"))
        self.assertEqual(str(test), '(\'Song\', \'name\') by (\'Artist\', \'Name\')')

    def test_song_create_picker(self):
        test = Song("Song", "Artist", "Thomas Bristow")
        self.assertEqual(test.picker, "Thomas Bristow")


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
        self.song_name = "test_song_name"
        self.alternate_song_name = "test_alternate_song_name"
        self.tertiary_song_name = "test_tertiary_song_name"
        self.forth_song_name = "test_forth_song_name"

        self.artist_name = "test_artist_name"
        self.alternate_artist_name = "test_alternate_artist_name"
        self.tertiary_artist_name = "test_tertiary_song_name"
        self.forth_artist_name = "test_forth_artist_name"

        self.picker = "first"
        self.alternate_picker = "second"
        self.tertiary_picker = "third"
        self.forth_picker = "forth"

        self.first_song = Song(self.song_name, self.artist_name, self.picker)
        self.second_song = Song(self.alternate_song_name, self.alternate_artist_name, self.alternate_picker)
        self.third_song = Song(self.tertiary_song_name, self.tertiary_artist_name, self.tertiary_picker)
        self.forth_song = Song(self.forth_song_name, self.forth_artist_name, self.forth_picker)

    def test_music_bracket_creation(self):
        for i in range(10):
            MusicBracket(2 ** (i + 1))

    def test_music_bracket_creation_bad_bracket_size_minus_input(self):
        self.assertRaises(ValueError, MusicBracket, -2)

    def test_music_bracket_creation_bad_bracket_size_invalid_input_odd(self):
        self.assertRaises(ValueError, MusicBracket, 13)

    def test_music_bracket_creation_bad_bracket_size_invalid_input_even(self):
        self.assertRaises(ValueError, MusicBracket, 20)

    def test_music_bracket_creation_bad_bracket_size_invalid_input_zero(self):
        self.assertRaises(ValueError, MusicBracket, 0)

    def test_music_bracket_add_song(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        self.assertEqual(test.songs, [self.first_song, self.second_song])

    def test_music_bracket_add_wildcard(self):
        test = MusicBracket(2)
        test.add_wildcard(self.first_song)
        test.add_wildcard(self.second_song)
        self.assertEqual(test.wildcard_songs, [self.first_song, self.second_song])

    def test_music_bracket_pick_random_wildcard_song(self):
        test = MusicBracket(2)
        test.add_wildcard(self.first_song)
        test.add_wildcard(self.second_song)
        for x in range(5):
            self.assertIn(test.pick_random_wildcard(),
                          [self.first_song, self.second_song])

    def test_music_bracket_get_picker(self):
        test = MusicBracket(4)
        self.forth_song.picker = "first"
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.add_song(self.third_song)
        test.add_song(self.forth_song)
        self.assertEqual(test.pickers, [{'Picker Name': 'first', 'Songs': 2},
                                        {'Picker Name': 'second', 'Songs': 1},
                                        {'Picker Name': 'third', 'Songs': 1}])

    def test_music_bracket_add_wildcard_to_songs(self):
        test = MusicBracket(2)
        test.add_wildcard(self.first_song)
        test.move_wildcard_to_songs()
        self.assertEqual(test.wildcard_songs, [])
        self.assertEqual(test.songs, [self.first_song])

    def test_music_bracket_add_wildcard_to_songs_double_wildcard(self):
        test = MusicBracket(2)
        test.add_wildcard(self.first_song)
        test.add_wildcard(self.second_song)
        test.move_wildcard_to_songs()
        self.assertEqual(len(test.wildcard_songs), 1)
        self.assertEqual(len(test.wildcard_songs), 1)

    def test_music_bracket_pick_random_song(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        for x in range(5):
            self.assertIn(test.pick_random_song(),
                          [self.first_song, self.second_song])

    def test_music_bracket_dictionary_output(self):
        test = MusicBracket(4)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.add_wildcard(self.third_song)
        test.add_wildcard(self.forth_song)
        self.assertEqual(test.output(), dict(Songs=[self.first_song, self.second_song],
                                             Wildcard_Songs=[self.third_song, self.forth_song],
                                             Bracket_Size=4))

    def test_music_bracket_create_bracket(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.create_bracket()
        self.assertIn(str(test.bracket), [str([Bracket(self.second_song,
                                                       self.first_song, 1)]),
                                          str([Bracket(self.first_song,
                                                       self.second_song, 1)])])

    def test_music_bracket_create_double_bracket(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.create_bracket()
        with self.assertRaises(Exception):
            test.create_bracket()

        test.add_song(self.third_song)
        test.add_song(self.forth_song)
        with self.assertRaises(Exception):
            test.create_bracket()

    def test_music_bracket_get_bracket(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.create_bracket()
        self.assertIn(test.get_bracket(),
                      [str(Bracket(self.first_song, self.second_song, 1)) + '\n',
                       str(Bracket(self.second_song, self.first_song, 1)) + '\n'])

    def test_music_bracket_get_empty_bracket(self):
        test = MusicBracket(2)
        with self.assertRaises(ValueError):
            test.create_bracket()

    def test_music_bracket_vote(self):
        test = MusicBracket(2)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.create_bracket()

        test.vote(0, 1, 2)
        self.assertEqual(test.bracket[0].song_b, test.bracket[0].winner)

        test.vote(0, 2, 1)
        self.assertEqual(test.bracket[0].song_a, test.bracket[0].winner)

        test.vote(0, 1, 1)
        self.assertIn(test.bracket[0].winner, [self.first_song, self.second_song])

    def test_music_bracket_vote_none_bracket(self):
        test = MusicBracket(2)
        with self.assertRaises(IndexError):
            test.vote(0, 1, 1)

    def test_music_bracket_promote(self):
        test = MusicBracket(4)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.add_song(self.third_song)
        test.add_song(self.forth_song)
        test.create_bracket()
        test.vote(0, 2, 1)
        test.vote(1, 2, 1)
        test.promote()
        self.assertEqual(test.bracket.__len__(), 3)
        self.assertIn(test.bracket[2].song_a, [self.first_song, self.second_song, self.third_song, self.forth_song])
        self.assertIn(test.bracket[2].song_b, [self.first_song, self.second_song, self.third_song, self.forth_song])
        self.assertNotEqual(test.bracket[2].song_a, test.bracket[2].song_b)

    def test_music_bracket_promote_none_bracket(self):
        test = MusicBracket(2)
        with self.assertRaises(IndexError):
            test.promote()

        test.add_song(self.first_song)
        test.add_song(self.second_song)
        with self.assertRaises(IndexError):
            test.promote()

        test.create_bracket()
        with self.assertRaises(IndexError):
            test.promote()

    def test_music_bracket_promote_none_winner(self):
        test = MusicBracket(4)
        test.add_song(self.first_song)
        test.add_song(self.second_song)
        test.add_song(self.third_song)
        test.add_song(self.forth_song)
        test.create_bracket()

        with self.assertRaises(ValueError):
            test.promote()

        test.vote(0, 1, 2)
        with self.assertRaises(ValueError):
            test.promote()


if __name__ == '__main__':
    unittest.main()
