from django.test import TestCase, Client
from api.models import Block, Address

class TestMeta(TestCase):

    def setUp(self):
        Block.objects.create(
            block_id='1234', number="3",
        )
        # Address.objects.create(
        #     wallet_id="1234",
        #     hash160="#123",
        #     version='1',
        #     balance='2:1',
        # )

    def test_block(self):
        block = Block.objects.get(id=1)
        self.assertEqual(block.block_id, "1234")
        self.assertEqual(block.number, "3")

    def test_block1(self):
        block = Block.objects.get(id=1)
        self.assertEqual(block.block_id, "1234")

    def test_block2(self):
        block = Block.objects.get(id=1)
        self.assertEqual(block.number, "3")
