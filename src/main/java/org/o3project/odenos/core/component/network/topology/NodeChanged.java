/*
 * Copyright 2015 NEC Corporation.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.o3project.odenos.core.component.network.topology;

import org.o3project.odenos.core.component.network.BaseNetworkChanged;

/**
 * NodeChanged represents a body of event message delivered when NodeChanged
 * event occurs.
 *
 */
public class NodeChanged extends BaseNetworkChanged<Node> {

  /**
   * Actions.
   *
   * <ul>
   * <li>add</li>
   * <li>delete</li>
   * <li>update</li>
   * </ul>
   */
  public static enum Action {
    add, delete, update;
  }

  public static final String TYPE = "NodeChanged";

  /**
   * Constructor.
   */
  public NodeChanged() {
    super(Node.class);
  }

  /**
   * Constructor.
   * @param prev previous node.
   * @param curr current node.
   * @param action string of action. "add", "delete", or "update"
   */
  public NodeChanged(final Node prev,
      final Node curr,
      final Action action) {
    super(action.name(), prev, curr);

    String id;
    String version = null;

    if (curr != null) {
      id = curr.getId();
      version = curr.getVersion();
    } else {
      id = prev.getId();
    }

    if (action == Action.delete) {
      version = null;
    }

    this.setId(id);
    this.setVersion(version);
  }
}