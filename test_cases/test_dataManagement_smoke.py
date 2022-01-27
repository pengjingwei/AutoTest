from unittest import TestCase

from selenium import webdriver

from pages.data_management.manage_metadata_synchronize import Synchronize
from pages.data_management.metamodel_addMetadata import AddMetaData
from pages.data_management.metamodel_createTable import CreateTable
from pages.data_management.metamodel_editField import metamodel_editField
from pages.data_management.metamodel_push import MetamodelPush

from pages.login import Login


class TestManage(TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_manage(self):
        login = Login(self.driver)
        login.login('admin', '123456')

        addMetadata = AddMetaData(self.driver)
        name = addMetadata.add()

        edit = metamodel_editField(self.driver)
        edit.editfield()

        create = CreateTable(self.driver)
        create.create_table(name)

        push = MetamodelPush(self.driver)
        res = push.push('ODS层的PAY_TEST')

        sync = Synchronize(self.driver)
        sync.synchronize()

        expect = '推送成功！'
        self.assertEqual(expect, res)
