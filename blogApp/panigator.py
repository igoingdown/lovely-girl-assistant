# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import collections
from math import ceil
from django.utils import six
from django.utils.functional import cached_property

class InvalidPage(Exception):
    pass


class PageNotAnInteger(InvalidPage):
    pass


class EmptyPage(InvalidPage):
    pass


class Panigator(object):

    def __init__(self, object_list, page_length, orphans=0,
                 allow_empty_first_page=True):
        self.object_list = object_list
        self.page_length = page_length
        self.orphans = orphans
        self.allow_empty_first_page = allow_empty_first_page

    def validate_number(self, num):
        try:
            num = int(num)
        except:
            raise PageNotAnInteger("Page num is not an integer")
        if num < 1:
            raise EmptyPage("Page num is less than 1")
        if num > self.num_pages:
            if num == 1 and self.allow_empty_first_page:
                pass
            else:
                raise EmptyPage("the page contains no results")

        return num

    @cached_property
    def num_pages(self):
        if self.count == 0 and not self.allow_empty_first_page:
            return 0
        hits = max(1, self.count - self.orphans)
        return  int(ceil(hits / float(self.page_length)))

    def page(self, num):
        num = self.validate_number(num)
        bottom = (num - 1) * self.page_length
        top = bottom + self.page_length
        if top + self.orphans >= self.count:
            top = self.count
        return self._get_page(self.object_list[bottom:top], num, self)

    def _get_page(self, *args, **kwargs):
        return Page(*args, **kwargs)

    @cached_property
    def count(self):
        try:
            return self.object_list.count()
        except (AttributeError, TypeError):
            return len(self.object_list)


class Page(collections.Sequence):
    def __init__(self, object_list, num, paginator):
        self.object_list = object_list
        self.num = num
        self.paginator = paginator

    def __repr__(self):
        return '<Page {0} of {1}>'.format(self.num, self.paginator.num_pages)

    def __len__(self):
        return len(self.object_list)

    def __getitem__(self, index):
        if not isinstance(index, (slice,) + six.integer_types):
            raise TypeError
        if not isinstance(self.object_list, list):
            self.object_list = list(self.object_list)
        return self.object_list[index]

    def has_next(self):
        return self.num < self.paginator.num_pages

    def has_previous(self):
        return self.num > 1

    def has_other_pages(self):
        return self.has_previous() or self.has_next()

    def next_page_num(self):
        return self.paginator.validate_number(self.num + 1)

    def previous_page_num(self):
        return self.paginator.validate_number(self.num - 1)

    def start_index(self):
        if self.paginator.count == 0:
            return  0
        return  (self.paginator.page_length * (self.num - 1)) + 1

    def end_index(self):
        if self.num == self.paginator.num_pages:
            return self.paginator.count
        return self.num * self.paginator.page_length


class CustomPaginator(Panigator):
    def __init__(self, cur_page, max_page_num_show, *args, **kwargs):
        self.cur_page = cur_page
        self.max_page_num_show = max_page_num_show
        super(CustomPaginator, self).__init__(*args, **kwargs)

    def page_num_range(self):
        if self.num_pages < self.max_page_num_show:
            return range(1, self.num_pages)
        half_part = int(self.max_page_num_show / 2)
        if self.cur_page < half_part:
            return range(1, self.max_page_num_show)
        print self.cur_page, type(self.cur_page)
        print half_part, type(half_part)
        print self.num_pages, type(self.num_pages)
        if (self.cur_page + half_part) > self.num_pages:
            return range(self.cur_page - self.max_page_num_show + 1, self.num_pages)
        return range(self.cur_page - half_part, self.cur_page + half_part + 1)



