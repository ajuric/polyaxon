# pylint:disable=ungrouped-imports

from unittest.mock import patch

import pytest

import activitylogs
import auditor
import tracker

from db.models.experiment_groups import ExperimentGroupChartView
from db.models.experiments import ExperimentChartView
from event_manager.events import chart_view as chart_view_events
from factories.factory_experiment_groups import ExperimentGroupFactory
from factories.factory_experiments import ExperimentFactory
from tests.utils import BaseTest


@pytest.mark.auditor_mark
class AuditorChartViewsTest(BaseTest):
    """Testing subscribed events"""
    DISABLE_RUNNER = True

    def setUp(self):
        super().setUp()
        self.experiment = ExperimentFactory()
        self.experiment_group = ExperimentGroupFactory()
        auditor.validate()
        auditor.setup()
        tracker.validate()
        tracker.setup()
        activitylogs.validate()
        activitylogs.setup()

    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_experiment_chart_view_created(self, activitylogs_record, tracker_record):
        chart_view = ExperimentChartView.objects.create(
            experiment=self.experiment,
            charts={}
        )
        auditor.record(event_type=chart_view_events.CHART_VIEW_CREATED,
                       instance=chart_view,
                       experiment=self.experiment,
                       actor_id=self.experiment.user.id,
                       actor_name=self.experiment.user.username)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1

    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_experiment_group_chart_view_created(self, activitylogs_record, tracker_record):
        chart_view = ExperimentGroupChartView.objects.create(
            experiment_group=self.experiment_group,
            charts={}
        )
        auditor.record(event_type=chart_view_events.CHART_VIEW_CREATED,
                       instance=chart_view,
                       experiment=self.experiment_group,
                       actor_id=self.experiment_group.user.id,
                       actor_name=self.experiment_group.user.username)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1

    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_experiment_chart_view_deleted(self, activitylogs_record, tracker_record):
        chart_view = ExperimentChartView.objects.create(
            experiment=self.experiment,
            charts={}
        )
        auditor.record(event_type=chart_view_events.CHART_VIEW_DELETED,
                       instance=chart_view,
                       experiment=self.experiment,
                       actor_id=self.experiment.user.id,
                       actor_name=self.experiment.user.username)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1

    @patch('tracker.service.TrackerService.record_event')
    @patch('activitylogs.service.ActivityLogService.record_event')
    def test_experiment_group_chart_view_deleted(self, activitylogs_record, tracker_record):
        chart_view = ExperimentGroupChartView.objects.create(
            experiment_group=self.experiment_group,
            charts={}
        )
        auditor.record(event_type=chart_view_events.CHART_VIEW_DELETED,
                       instance=chart_view,
                       experiment=self.experiment_group,
                       actor_id=self.experiment_group.user.id,
                       actor_name=self.experiment_group.user.username)

        assert tracker_record.call_count == 1
        assert activitylogs_record.call_count == 1
