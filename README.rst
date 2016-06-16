This is a plugin intended to extend the functionality of the `metadata_extractor` plugin for [girder](https://github.com/girder/girder).

To try it out, clone to the `plugins` directory of `girder`

::

   cd /path/to/girder/plugins
   git clone https://github.com/0x414A/metadata_extractor_plus


Install the required python libraries and modules:

::

   pip install -r requirements.txt


If you want to test out the development version of ``yt`` with the metadata extractor:

::

   pip install --upgrade 'hg+https://bitbucket.org/yt_analysis/yt@yt#egg=yt'


Then from the "Admin console" enable "Metadata Extractor Plus".

*NOTE* I can't get the extractor to fire off just yet. But you can test it by uploading a `yt`-supported dataset.

Then, navigate to the girder item page. e.g. http://localhost:8080/#item/57632981e640ae56cbf20ec9

That string after ``item/`` is the ``itemId`` you'll need below. Replace ``<path-to-dataset>`` with the local path to the dataset.

Example:

::
   
   ./test.py -p <path-to-dataset> -i <itemId>

