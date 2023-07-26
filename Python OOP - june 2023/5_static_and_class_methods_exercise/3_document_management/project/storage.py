from typing import List
from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic:Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document:Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        category = [c for c in self.categories if c.id == category_id][0]
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        e_topic = [t for t in self.topics if t.id == topic_id][0]
        e_topic.topic = new_topic
        e_topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        doc= [d for d in self.documents if d.id == document_id][0]
        doc.file_name = new_file_name

    def delete_category(self, category_id):
        category = [c for c in self.categories if c.id == category_id][0]
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        d_topic = [t for t in self.topics if t.id == topic_id][0]
        self.topics.remove(d_topic)

    def delete_document(self, document_id):
        del_doc = [d for d in self.documents if d.id == document_id][0]
        self.documents.remove(del_doc)

    def get_document(self, document_id):
        get_doc = [d for d in self.documents if d.id == document_id][0]
        return get_doc

    def __repr__(self):
        result = ''
        for dd in self.documents:
            result += f"{dd}\n"
        return result


