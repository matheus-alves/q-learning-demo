# coding=utf8
import wx
import wx.grid

from gui import gridinfo
from qlearning import Actions


class GridFrame(wx.Frame):

    def _generate_grid(self, results):
        """
        Generates the results grid
        """

        # Creates a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Sets the dimensions of the grid
        grid.CreateGrid(gridinfo.NUM_OF_ROWS, gridinfo.NUM_OF_COLUMNS)

        # Sets the sizes of individual rows and columns in pixels
        for i in range(0, gridinfo.NUM_OF_ROWS):
            grid.SetRowSize(i, gridinfo.CELL_SIZE)

        for i in range(0, gridinfo.NUM_OF_COLUMNS):
            grid.SetColSize(i, gridinfo.CELL_SIZE)

        # Removes the labels
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(0)

        # Creates the penalty states
        for state in gridinfo.PENALTY:
            grid.SetCellBackgroundColour(state[0], state[1], wx.BLUE)

        # Creates the start and goal states
        grid.SetCellValue(gridinfo.START[0], gridinfo.START[1], 'S')
        grid.SetCellFont(gridinfo.START[0], gridinfo.START[1],
                         wx.Font(24, wx.ROMAN, wx.NORMAL, wx.NORMAL))
        grid.SetCellValue(gridinfo.GOAL[0], gridinfo.GOAL[1], 'G')
        grid.SetCellFont(gridinfo.GOAL[0], gridinfo.GOAL[1],
                         wx.Font(24, wx.ROMAN, wx.NORMAL, wx.NORMAL))

        # Prints the results on the grid
        for q in results:
            grid.SetCellBackgroundColour(q[0], q[1], wx.RED)

        return grid

    def generate_action_grid(self, q_values, action):
        """
        Generates a grid for each action
        """

        # Creates a wxGrid object
        grid = wx.grid.Grid(self, -1)

        # Sets the dimensions of the grid
        grid.CreateGrid(gridinfo.NUM_OF_ROWS, gridinfo.NUM_OF_COLUMNS)

        # Removes the labels
        grid.SetRowLabelSize(0)
        grid.SetColLabelSize(0)

        # Sets the values of each cell
        for q in q_values:
            if q[2] == action:
                grid.SetCellValue(q[0], q[1], str(q_values[q]))
                grid.SetReadOnly(q[0], q[1], True)

        return grid

    def __init__(self, parent, id, title, results, q_values, type):
        wx.Frame.__init__(self, parent, id, title)

        if (type == 1):
            print('\nGenerating results')

            # Defines the grid size
            sizer = wx.BoxSizer()
            sizer.Add(self._generate_grid(results), 1, wx.EXPAND | wx.ALL)

            self.SetSizerAndFit(sizer)
            self.Show()

        if (type == 2):
            sizer = wx.BoxSizer(wx.VERTICAL)

            for action in Actions:
                if action == Actions.up:
                    text = wx.StaticText(self, wx.ID_ANY, 'UP:')
                    sizer.Add(text, 1, wx.CENTER)
                elif action == Actions.down:
                    text = wx.StaticText(self, wx.ID_ANY, 'DOWN:')
                    sizer.Add(text, 1, wx.CENTER)
                elif action == Actions.left:
                    text = wx.StaticText(self, wx.ID_ANY, 'LEFT:')
                    sizer.Add(text, 1, wx.CENTER)
                elif action == Actions.right:
                    text = wx.StaticText(self, wx.ID_ANY, 'RIGHT:')
                    sizer.Add(text, 1, wx.CENTER)

                sizer.Add(self.generate_action_grid(
                    q_values, action), 1, wx.EXPAND)

            self.SetSizerAndFit(sizer)
            self.Show()
