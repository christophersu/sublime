import sublime
import sublime_plugin
from git import GitTextCommand

class GitCommitAllCommand(GitTextCommand):
    def run(self, edit):
        self.run_command(['git', 'commit', '-a', '-m', 'External editor'])