import unittest
from SI506W18_ps8 import *

print("*************\n")
##### Code for running tests is below this line. Don't change any code below this line!######

class Problem1(unittest.TestCase):
    def test_sample_photo_rep(self):
        self.assertEqual(sample_photo_rep,{u'photo': {u'people': {u'haspeople': 0}, u'dateuploaded': u'1467709435', u'owner': {u'username': u'Ansel Adams', u'realname': u'', u'path_alias': None, u'iconserver': u'7332', u'nsid': u'48093195@N03', u'location': u'', u'iconfarm': 8}, u'publiceditability': {u'canaddmeta': 1, u'cancomment': 1}, u'id': u'27820301400', u'title': {u'_content': u'Photo1'}, u'media': u'photo', u'tags': {u'tag': [{u'machine_tag': False, u'_content': u'nature', u'author': u'48093195@N03', u'raw': u'Nature', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-5470'}, {u'machine_tag': False, u'_content': u'mist', u'author': u'48093195@N03', u'raw': u'Mist', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-852'}, {u'machine_tag': False, u'_content': u'mountain', u'author': u'48093195@N03', u'raw': u'Mountain', u'authorname': u'ac | photo albums', u'id': u'48070141-27820301400-1695'}]}, u'comments': {u'_content': u'0'}, u'secret': u'c86034becf', u'usage': {u'canblog': 0, u'canshare': 1, u'candownload': 0, u'canprint': 0}, u'description': {u'_content': u''}, u'isfavorite': 0, u'views': u'4', u'farm': 8, u'visibility': {u'isfriend': 0, u'isfamily': 0, u'ispublic': 1}, u'rotation': 0, u'dates': {u'taken': u'2016-07-05 11:03:52', u'takenunknown': u'1', u'posted': u'1467709435', u'lastupdate': u'1467709679', u'takengranularity': 0}, u'license': u'0', u'notes': {u'note': []}, u'server': u'7499', u'safety_level': u'0', u'urls': {u'url': [{u'type': u'photopage', u'_content': u'https://www.flickr.com/photos/48093195@N03/27820301400/'}]}, u'editability': {u'canaddmeta': 0, u'cancomment': 0}}, u'stat': u'ok'})

class Problem3(unittest.TestCase):
    def test_sample_tags_list(self):
        self.assertEqual(sample_tags_list,[u'nature', u'mist', u'mountain'])

class Problem4(unittest.TestCase):
    def test_search_result_diction(self):
        self.assertIsInstance(search_result_diction,dict, "Testing that search_result_diction is a dictiionary")
    def test_search_result_diction2(self):
        self.assertTrue("photos" in search_result_diction, "Testing that the photos key is in the loaded flickr response, as it should be")
    def test_sample_photo_ids(self):
        self.assertIsInstance(sample_photo_ids,list,"Testing that sample_photo_ids is a list")
    def test_sample_photo_ids2(self):
        self.assertTrue(sample_photo_ids[2] != sample_photo_ids[23], "Testng that not all the sample photo ids are the same id")
    def test_sample_photo_ids3(self):
        self.assertEqual(len(sample_photo_ids),50,"Testing there are 50 photo ids in the sample_photo_ids list")

class Problem5(unittest.TestCase):
    def test_cache_diction_existence(self):
        self.assertIsInstance(CACHE_DICTION,dict,"Testing that cache_diction is a dictionary")

class Problem6(unittest.TestCase):
    def test_get_flickr_data1(self):
        self.assertEqual(sorted(list(get_flickr_data("alps").keys())),sorted([u'photos', u'stat']), "Testing the keys of the return value of get_flickr_data")
    def test_get_flickr_data2(self):
        self.assertEqual(sorted(list(get_flickr_data("alps")["photos"]["photo"][49].keys())),sorted([u'isfamily', u'title', u'farm', u'ispublic', u'server', u'isfriend', u'secret', u'owner', u'id']), "Testing the keys of one of the photos inside the get_flickr_data response")
    def test_get_flickr_data_resp_type(self):
        self.assertIsInstance(get_flickr_data("alps")["photos"]["photo"][49],dict, "Testing that the value of one of the photos in the function's return value is a dictionary")
    def test_get_all_diff_photos(self):
        self.assertTrue(get_flickr_data("sunset")["photos"]["photo"][30]["id"] != get_flickr_data("sunset")["photos"]["photo"][15]["id"], "Testing that the list of photos is not a composed list of all the same photo")
    def test_default_num_photos(self):
        self.assertEqual(len(get_flickr_data("sunset")["photos"]["photo"]),50,"Testing that the default num_photos response has 50 photos")
    def test_cache_in_function(self):
        testfile = open("pset8_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("mountains" in testfilestr,"Testing that the mountains request was cached")
    def test_cache_in_function2(self):
        testfile = open("pset8_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("per_page-50" in testfilestr, "Testing (in part) that the params_unique_combination was used properly in the cache setup")
    def test_cache_in_function3(self):
        get_flickr_data("summer 2013",112) # specific params
        testfile = open("pset8_cached_data.json","r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue("https://api.flickr.com/services/rest/format-json_method-flickr.photos.search_per_page-112_tag_mode-all_tags-summer 2013" in testfilestr, "Testing that params and unique identifer setup are correct in get_flickr_data function")

class Problem7(unittest.TestCase):
    def test_flickr_mountains_result_keys(self):
        self.assertEqual(sorted(list(flickr_mountains_result.keys())),sorted([u'photos', u'stat']),"Testing the keys of the value of flickr_mountains_result, which should be a dictionary")
    def test_fmr_res_type(self):
        self.assertEqual(type(flickr_mountains_result),type({}),"Testing that the type of flickr_mountains_result is a dictionary")
    def test_num_photos_flickr_mountains_res(self):
        self.assertEqual(len(flickr_mountains_result["photos"]["photo"]),50,"Testing that there are 50 photos in flickr_mountains_result")

class Problem8(unittest.TestCase):
    def test_photo_ids_len(self):
        self.assertEqual(len(photo_ids),50,"Testing that there are 50 photo ids")
    def test_diff_photo_ids(self):
        self.assertTrue(photo_ids[0] != photo_ids[40], "Testing that the photo ids are different, not just 50 of the same one (check out your nested iteration, maybe)")
    def test_ids_in_cache(self):
        testfile = open(CACHE_FNAME,"r")
        testfilestr = testfile.read()
        testfile.close()
        self.assertTrue(photo_ids[4] in testfilestr,"Testing that one of the ids, like the other response data, is inside the cache file")

class Problem9(unittest.TestCase):
    def test_problem9_invocation(self):
        self.assertTrue(get_photo_data_with_caching("33119881551"))
    def test_problem9_data(self):
        self.assertEqual(sorted(list(get_photo_data_with_caching("33119881551").keys())),sorted(["photo","stat"]) )



if __name__ == "__main__":
    unittest.main(verbosity=2)
