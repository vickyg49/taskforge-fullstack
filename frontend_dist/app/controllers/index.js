import Controller from '@ember/controller';
import { action } from '@ember/object';
import { tracked } from '@glimmer/tracking';
import { inject as service } from '@ember/service';

export default class IndexController extends Controller {
  @service api;

  @tracked title = '';
  @tracked description = '';
  // model is provided by the route (this.model)

  @action updateTitle(e) { this.title = e.target.value; }
  @action updateDescription(e) { this.description = e.target.value; }

  @action
  async createTask(e) {
    e.preventDefault();
    const payload = { title: this.title, description: this.description };
    const created = await this.api.createTask(payload);
    this.model = [created, ...(this.model || [])];
    this.title = '';
    this.description = '';
  }

  @action
  async cycleStatus(task) {
    const next = task.status === 'todo' ? 'inprogress' : (task.status === 'inprogress' ? 'done' : 'todo');
    const updated = await this.api.updateTask(task.id, { ...task, status: next });
    this.model = this.model.map(t => (t.id === updated.id ? updated : t));
  }

  @action
  async deleteTask(task) {
    await this.api.deleteTask(task.id);
    this.model = this.model.filter(t => t.id !== task.id);
  }
}
