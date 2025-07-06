"""Module interface.py"""
import src.data.interface
import src.elements.master as mr
import src.elements.s3_parameters as s3p
import src.preface.interface


class Interface:
    """
    Reads-in FEW NERD (Few-Shot Named Entity Recognition Data)
    """

    def __init__(self):
        """
        Constructor
        """

        self.__s3_parameters: s3p
        _, self.__s3_parameters, _ = src.preface.interface.Interface().exc()

    def exc(self) -> mr.Master:
        """

        :return:
        """

        # Get data & labels
        master: mr.Master = src.data.interface.Interface(
            s3_parameters=self.__s3_parameters).exc()

        return master
