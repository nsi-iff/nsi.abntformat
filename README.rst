nsi.abntformat
==============

Transforma objetos contendo metadados de documentos em referências bibliográficas
no formato ABNT.

Com suporte a:

- trabalho de conclusão
- artigo de anais de eventos
- artigo de periódico
- periódico técnico científico
- livro
- relatório técnico científico


Como instalar
-------------

::

    $ pip install nsi.abntformat


Como usar
---------

No exemplo abaixo, é gerada uma referência bibliográfica para trabalho de conclusão::

    >>> from nsi.abntformat import ReferenciaBibliografica

    >>> class Documento(object): pass
    >>> documento = Documento()
    >>> documento.tipo = 'trabalho de conclusão'
    >>> documento.autores = 'Linus Torvalds'
    >>> documento.titulo = 'Git'
    >>> documento.subtitulo = 'Destruindo o Passado de Trevas'
    >>> documento.data_defesa = 2008
    >>> documento.total_folhas = 120
    >>> documento.tipo_trabalho = 'Tese (Doutorado em Computacao)'
    >>> documento.instituicao = 'Instituto Federal Fluminense'
    >>> documento.local_defesa = 'Campos dos Goytacazes/RJ'
    >>> referencia = ReferenciaBibliografica()
    >>> referencia.gerar(documento)
    'TORVALDS, L. Git: Destruindo o Passado de Trevas. 2008. 120 f. Tese (Doutorado em Computacao) - Instituto Federal Fluminense, Campos dos Goytacazes/RJ.'

Copyright
---------

Copyright (c) 2011 Núcleo de Pesquisa em Sistemas de Informação. Veja LICENSE.txt para mais informações.
