import Route from '@ember/routing/route';
import { inject as service } from '@ember/service';

export default class IndexRoute extends Route {
  @service api;
  async model() {
    // Loads tasks from Django
    return await this.api.getTasks();
  }
}
