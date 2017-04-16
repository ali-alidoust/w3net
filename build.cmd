@ECHO off
RD /S /Q .\dist

pyinstaller build.spec