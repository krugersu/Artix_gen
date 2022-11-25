
Разные примечания
=================

PRAGMA synchronous
Как было написано выше, по умолчанию база SQLite создается с настройками максимальной безопасности. В частности, флаг  synchronous установлен в значение FULL. Использование этого значения гарантирует вам, что все данные будут записаны в базу данных и авария или сбой питания не нарушат целостность базы данных. Однако за такую гарантию мы «платим» временем.

synchronous может принимать три значения:

0 | OFF — синхронизация БД полностью отключена. При таком режиме работы, в случае аварии, возможен выход из строя базы данных
1 | NORMAL — в этом случае SQLite синхронизирует данные только в самых критичных ситуациях и синхронизация запускается намного реже, чем при режиме FULL.
2 | FULL — максимальный уровень безопасности.
Таким образом, в зависимости от ваших требований к безопасности работы БД, можно «поиграть» с флагом synchronous и ускорить время записи данных. 

Как можно менять значения PRAGMA при использовании LiteDAC? Собственно, как и при использовании любых других компонентов для работы с SQLite. Например, так:

LiteConnection1.ExecSQL('PRAGMA synchronous = OFF';


После установки всё заработало (sqlite3)
****************************************

Option 1: Use the binary version of pysqlite3 from here 
(which already comes with a newer version of sqlite3 lib precompiled and linked): https://github.com/coleifer/pysqlite3. Basically install with

::

    pip install pysqlite3-binary
::

and in python code, use pysqlite3 instead of sqlite3 like:

::

    import
        pysqlite3
        (...) conn = pysqlite3.connect(r"filename")

::

Alternative: Reinstall python, when installing python, a built in python's module sqlite3 (for working with sqlite) is compiling and uses (compiles) its own version of sqlite3 lib regardless of what you currently have in your system (this is the case at least on windows and mac systems, may be also the case for unix based systems).
