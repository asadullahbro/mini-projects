# ccwc - Mini Word Count CLI Tool

`ccwc` is a small Python command-line tool inspired by the Unix `wc` command.  
It can count lines, words, bytes, and characters in a text file.

## Usage

```bash
python ccwc.py [OPTION] <filename>
```
If no option is given, it prints lines, words, and bytes by default.
• `-c`: count bytes

• `-m`: count characters

• `-w`: count words

• `-l`: count lines

## Examples

Default (lines, words, bytes):
```bash
python ccwc.py test.txt
```
Count words only:
```bash
python ccwc.py -w test.txt
```
Count characters:
```bash
python ccwc.py -m test.txt
```
Count bytes:
```bash
python ccwc.py -c test.txt
```
## Notes
• Make sure the file exists, otherwise it will show an error.

• Words with UTF-8 encoded files.
