from abc import abstractmethod
from pathlib import Path
from typing import Iterator

from .core import VcsFileSystemIdentifier, VcsProviderFactory


class GitCommonVcsProviderFactory(VcsProviderFactory):
    __git_dir_provider = VcsFileSystemIdentifier(file_name=None, dir_name=".git")
    __git_wt_file_provider = VcsFileSystemIdentifier(file_name=".git", dir_name=None)

    @abstractmethod
    def _create_provider(self, path: Path) -> VcsProvider:
        raise NotImplementedError()

    @property()
    def vcs_fs_root(self) -> Iterator[VcsFileSystemIdentifier]:
        yield self.__git_dir_provider
        yield self.__git_wt_file_provider
