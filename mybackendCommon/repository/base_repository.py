from abc import ABC, abstractmethod


class RepositoryAsset(ABC):
    @abstractmethod
    def get(self, asset_id):
        raise NotImplementedError

    @abstractmethod
    def get_all(self):
        raise NotImplementedError

    @abstractmethod
    def create(self, asset):
        raise NotImplementedError

    @abstractmethod
    def update(self, asset_id, update_info):
        pass

    @abstractmethod
    def delete(self, asset_id):
        pass
