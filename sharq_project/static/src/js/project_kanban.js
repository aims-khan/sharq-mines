/** @odoo-module **/

import KanbanRenderer from 'web.KanbanRenderer';
import KanbanView from 'web.KanbanView';
import KanbanRecord from 'web.KanbanRecord';
import viewRegistry from 'web.view_registry';

// PROJECTS

const SharqProjectProjectKanbanRecord = KanbanRecord.extend({
    /**
     * @override
     * @private
     */
    _openRecord: function () {
        this._super.apply(this, arguments);
    },
    /**
     * @override
     * @private
     */
    _onManageTogglerClicked: function (event) {
        this._super.apply(this, arguments);
        const thisSettingToggle = this.el.querySelector('.o_kanban_manage_toggle_button');
        this.el.parentNode.querySelectorAll('.o_kanban_manage_toggle_button.show').forEach(el => {
            if (el !== thisSettingToggle) {
                el.classList.remove('show');
            }
        });
        thisSettingToggle.classList.toggle('show');
    },
});


const SharqProjectProjectKanbanRenderer = KanbanRenderer.extend({
    config: _.extend({}, KanbanRenderer.prototype.config, {
        KanbanRecord: SharqProjectProjectKanbanRecord,
    }),
});

const SharqProjectProjectKanbanView = KanbanView.extend({
    config: Object.assign({}, KanbanView.prototype.config, {
        Renderer: SharqProjectProjectKanbanRenderer,
    })
});

viewRegistry.add('sharq_project_kanban', SharqProjectProjectKanbanView);
