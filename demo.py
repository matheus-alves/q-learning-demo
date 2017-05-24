import sys
import wx

from gui import gui
import qlearning


def main(args=sys.argv):
    episodes = 0
    if len(args) > 1:
        episodes = int(args[1])

    # Calculates the q-learning results
    results = qlearning.apply_q_learning(episodes)

    # Creates the UI to show the results
    app = wx.App(0)
    gui.GridFrame(None, -1, 'Q Values', results, qlearning.get_q_values(), 2)
    gui.GridFrame(None, -1, 'Q-Learning Results',
                  results, qlearning.get_q_values(), 1)
    app.MainLoop()


if __name__ == '__main__':
    main()
