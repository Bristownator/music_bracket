import unittest

from src.music_bracket import Song, MusicBracket


class StandardItems:
    def standard_bracket(self):
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


class SongTests(unittest.TestCase):

    def create_song_test(self):
        test = Song("test_song_name", "test_artist_name")
        self.assertEqual(test, "test_song_name by test_artist_name")


if __name__ == '__main__':
    unittest.main()
