import unittest
from dynamics_atlas_harness.q16_source_extract_v2 import extract_processed_roles

class SourceRoleTests(unittest.TestCase):
    def cells(self):
        return {f'{column}{row}':{'type':'n','value':value}
            for row in range(5,65) for column,value in [('A',(row-5)*.032),('B',1-row*.001),('C',.9)]}

    def test_fit_missing_tail_or_interior_does_not_select_observations(self):
        for removed in [list(range(45,65)), [20]]:
            cells = self.cells()
            baseline = extract_processed_roles(cells,'A','B','C')
            for row in removed:
                del cells[f'C{row}']
            result = extract_processed_roles(cells,'A','B','C')
            self.assertEqual(result['processed'], baseline['processed'])
            self.assertEqual(result['selection_audit']['previously_excluded_observed_rows'], removed)
            self.assertEqual(len(result['fit_audit']), 60-len(removed))

    def test_missing_observation_does_not_remove_independent_fit(self):
        cells = self.cells()
        del cells['B20']
        result = extract_processed_roles(cells,'A','B','C')
        self.assertEqual(len(result['processed']),59)
        self.assertEqual(len(result['fit_audit']),60)
        self.assertNotIn(20,result['selection_audit']['observed_rows'])

    def test_fit_value_cannot_change_observations(self):
        cells = self.cells()
        baseline = extract_processed_roles(cells,'A','B','C')['processed']
        cells['C20']['value'] = 123456
        self.assertEqual(extract_processed_roles(cells,'A','B','C')['processed'],baseline)

if __name__ == '__main__':
    unittest.main()
